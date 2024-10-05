# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "feedparser",
#     "rich",
#     "typer",
# ]
# ///

import feedparser
import re
import typer
from pathlib import Path


def fetch_rss_feed(*, url: str):
    """Fetch and parse the RSS feed."""
    return feedparser.parse(url)


def format_entry(*, entry):
    """Format a single RSS entry."""
    return f"- [{entry.title}]({entry.link})"


def update_readme(
    *,
    feed_entries: str,
    limit: int,
    readme_path: str,
    section: str,
):
    """Update the README.md file with new RSS feed entries."""
    content = Path(readme_path).read_text()

    # Define start and end markers
    start_marker = f"<!--START_SECTION:{section}-->"
    end_marker = f"<!--END_SECTION:{section}-->"

    # Create the new content
    new_content = "\n".join(
        [format_entry(entry=entry) for entry in feed_entries[:limit]]
    )  # Last 5 entries

    # Replace the content between markers
    pattern = f"{start_marker}.*?{end_marker}"
    replacement = f"{start_marker}\n{new_content}\n{end_marker}"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Write the updated content back to the file
    content = Path(readme_path).write_text(updated_content)


def main(
    rss_url: str, section: str = "news", readme_path: str = "README.md", limit: int = 5
):
    # Fetch the RSS feed
    feed = fetch_rss_feed(url=rss_url)

    # Update the README
    update_readme(
        feed_entries=feed.entries, limit=limit, readme_path=readme_path, section=section
    )


if __name__ == "__main__":
    typer.run(main)
