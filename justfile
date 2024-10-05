export JUST_UNSTABLE := "true"

@_default:
    just --list

@fmt:
    just --fmt

@bootstrap:
    python -m pip install --upgrade pip uv

@fetch-rss:
    # Fetch latest Django News Newsletter entries
    uv run fetch-rss.py \
        --section=news \
        --readme-path=profile/README.md \
        https://django-news.com/issues.rss

    # Fetch latest Django News Jobs entries
    uv run fetch-rss.py \
        --section=jobs \
        --readme-path=profile/README.md \
        https://jobs.django-news.com/feed/

    # Fetch latest Django TV entries
    uv run fetch-rss.py \
        --section=videos \
        --readme-path=profile/README.md \
        https://djangotv.com/feeds/

@lint *ARGS:
    uv run --with pre-commit-uv pre-commit run {{ ARGS }} --all-files
