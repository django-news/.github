export JUST_UNSTABLE := "true"

@_default:
    just --list

@fmt:
    just --fmt

@bootstrap:
    python -m pip install --upgrade pip uv
    uv pip install --requirement requirements.in

@fetch-rss:
    uv run fetch-rss.py \
        --section=news \
        --readme-path=profile/README.md \
        https://django-news.com/issues.rss

    uv run fetch-rss.py \
        --section=jobs \
        --readme-path=profile/README.md \
        https://jobs.django-news.com/feed/

@lint:
    uv tool run black .
