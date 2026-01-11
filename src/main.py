import os
import sys
from dotenv import load_dotenv
from anthropic import Anthropic
from rich.console import Console
from rich.panel import Panel

# אתחול הדפסה יפה לטרמינל
console = Console()

def load_environment():
    """טעינת משתני סביבה וביצוע בדיקות תקינות"""
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        console.print("[bold red]ERROR:[/bold red] Missing ANTHROPIC_API_KEY in .env file")
        return None
    
    return api_key

def read_file_content(filepath):
    """קריאת תוכן קובץ טקסט/מרקדאון"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        console.print(f"[bold red]ERROR:[/bold red] File not found: {filepath}")
        return None

def test_connection(client):
    """בדיקת תקשורת בסיסית מול קלוד"""
    console.print("[yellow]Testing connection to Claude...[/yellow]")
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-latest", 
            max_tokens=100,
            temperature=0.7,
            messages=[
                {"role": "user", "content": "Say 'System Online' and give me a random quote about creativity."}
            ]
        )
        response_text = message.content[0].text
        console.print(Panel(response_text, title="Claude Response", border_style="green"))
        return True
    except Exception as e:
        console.print(f"[bold red]Connection Failed:[/bold red] {e}")
        return False

def main():
    console.print("[bold blue]Project Ouroboros - Initialization[/bold blue]")
    
    # 1. Setup
    api_key = load_environment()
    if not api_key:
        return

    try:
        client = Anthropic(api_key=api_key)
    except Exception as e:
        console.print(f"[red]Error initializing Anthropic client: {e}[/red]")
        return
    
    # 2. Load Knowledge Base (Test)
    dna_path = "00_knowledge_base/client_dna.md"
    console.print(f"Loading DNA from: [underline]{dna_path}[/underline]...")
    dna_content = read_file_content(dna_path)
    
    if dna_content:
        console.print(f"[green]SUCCESS:[/green] DNA Loaded ({len(dna_content)} chars)")
    else:
        console.print("[red]WARNING:[/red] DNA file could not be loaded.")

    # 3. API Test
    test_connection(client)

if __name__ == "__main__":
    main()
