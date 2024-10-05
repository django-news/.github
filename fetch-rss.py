# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "feedparser",
#     "rich",
#     "typer",
# ]
# ///

import feedparser
import os
import re
import typer


def fetch_rss_feed(url: str):
    """Fetch and parse the RSS feed."""
    return feedparser.parse(url)


def format_entry(entry):
    """Format a single RSS entry."""
    return f"- [{entry.title}]({entry.link})"


def update_readme(feed_entries: str, section: str, readme_path: str):
    """Update the README.md file with new RSS feed entries."""
    with open(readme_path, "r") as file:
        content = file.read()

    # Define start and end markers
    # start_marker = "<!-- RSS_FEED_START -->"
    # end_marker = "<!-- RSS_FEED_END -->"
    start_marker = f"<!--START_SECTION:{section}-->"
    end_marker = f"<!--END_SECTION:{section}-->"

    # Create the new content
    new_content = "\n".join(
        [format_entry(entry) for entry in feed_entries[:5]]
    )  # Last 5 entries

    # Replace the content between markers
    pattern = f"{start_marker}.*?{end_marker}"
    replacement = f"{start_marker}\n{new_content}\n{end_marker}"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Write the updated content back to the file
    with open(readme_path, "w") as file:
        file.write(updated_content)


def main(rss_url: str, section: str = "news", readme_path: str = "README.md"):
    # Fetch the RSS feed
    feed = fetch_rss_feed(rss_url)

    # Update the README
    update_readme(feed_entries=feed.entries, section=section, readme_path=readme_path)


if __name__ == "__main__":
    typer.run(main)
