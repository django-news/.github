export JUST_UNSTABLE := "true"

@_default:
    just --list

@bootstrap:
    python -m pip install --upgrade pip uv

@fetch-rss:
    # Fetch latest Django News Newsletter entries
    uv run fetch-rss.py \
        --section=news \
        --readme-path=profile/README.md \
        https://django-news.com/issues.rss

    # Fetch latest Django Job Board entries
    uv run fetch-rss.py \
        --section=jobs \
        --readme-path=profile/README.md \
        https://djangojobboard.com/feed/

    # Fetch latest Django TV entries
    uv run fetch-rss.py \
        --section=videos \
        --readme-path=profile/README.md \
        https://djangotv.com/feeds/

@fmt:
    just --fmt

@lint *ARGS:
    uv run --with pre-commit-uv pre-commit run {{ ARGS }} --all-files
