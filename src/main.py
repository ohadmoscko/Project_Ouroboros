import os
import sys
try:
    from dotenv import load_dotenv
    from anthropic import Anthropic
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    print("Error: Libraries not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

console = Console()

def main():
    console.print("[bold blue]Project Ouroboros - SYSTEM CHECK[/bold blue]")
    
    # 1. בדיקת מפתח
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        console.print("[bold red]ERROR: Missing API Key in .env file![/bold red]")
        console.print("[yellow]Tip: copy `.env.sample` to `.env` and set `ANTHROPIC_API_KEY`.[/yellow]")
        sys.exit(1)

    # 2. בדיקת קובץ DNA
    if os.path.exists("00_knowledge_base/client_dna.md"):
        console.print("[green]V[/green] DNA File found.")
    else:
        console.print("[red]X[/red] DNA File missing.")

    # 3. בדיקת קלוד
    console.print("[yellow]Calling Claude...[/yellow]")
    model_env = os.getenv("ANTHROPIC_MODEL")
    if not model_env:
        console.print("[yellow]Warning: `ANTHROPIC_MODEL` not set. Trying default 'claude-2'. To avoid surprises, set `ANTHROPIC_MODEL` in your .env (see `.env.sample`).[/yellow]")
    model = model_env or "claude-2"
    try:
        client = Anthropic(api_key=api_key)
        message = client.messages.create(
            model=model,
            max_tokens=50,
            messages=[{"role": "user", "content": "Just say: 'System is ready' in Hebrew"}]
        )
        console.print(Panel(message.content[0].text, title=f"Claude ({model})", border_style="green"))
    except Exception as e:
        msg = str(e).lower()
        if "not_found" in msg or ("model" in msg and "not found" in msg) or ("model" in msg and "not_found" in msg):
            console.print(f"[yellow]Model '{model}' not found. Attempting common fallbacks: claude-2, claude-3, claude-4...[/yellow]")
            fallbacks = ["claude-2", "claude-3", "claude-4"]
            tried = []
            for fm in fallbacks:
                if fm == model:
                    continue
                tried.append(fm)
                try:
                    message = client.messages.create(
                        model=fm,
                        max_tokens=50,
                        messages=[{"role": "user", "content": "Just say: 'System is ready' in Hebrew"}]
                    )
                    console.print(Panel(message.content[0].text, title=f"Claude ({fm})", border_style="green"))
                    console.print(f"[green]Switched to model '{fm}'[/green]")
                    break
                except Exception:
                    continue
            else:
                console.print(f"[bold red]Connection Error:[/bold red] Model '{model}' not found. Tried fallbacks: {', '.join(tried)}. Set `ANTHROPIC_MODEL` in your .env to a valid model name or check your Anthropic account.")
                sys.exit(1)
        elif "unauthorized" in msg or "401" in msg or "invalid api key" in msg:
            console.print("[bold red]Connection Error:[/bold red] API key invalid or unauthorized. Check `ANTHROPIC_API_KEY` in your .env and your Anthropic account.")
            sys.exit(1)
        else:
            console.print(f"[bold red]Connection Error:[/bold red] {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
