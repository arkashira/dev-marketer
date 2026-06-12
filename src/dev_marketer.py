import json
import datetime
from dataclasses import asdict, dataclass
from typing import List, Dict


@dataclass
class SocialPost:
    platform: str
    content: str
    scheduled_date: str  # ISO format


def _generate_copy(product_name: str) -> str:
    """Return a short marketing copy for the product."""
    return (
        f"Introducing **{product_name}** – the simplest way to "
        f"solve your problem. Get started today and experience the difference!"
    )


def _create_landing_page(product_name: str) -> str:
    """
    Simulate landing page creation.
    Returns a deterministic subdomain URL.
    """
    slug = product_name.lower().replace(" ", "-")
    return f"https://{slug}.dev-marketer.axentx.com"


def _provision_email_list(product_name: str) -> str:
    """
    Simulate provisioning an email list.
    Returns a deterministic identifier.
    """
    # Simple deterministic hash (modulo to keep it short)
    list_id = f"list_{abs(hash(product_name)) % 10000}"
    return list_id


def _draft_welcome_email(product_name: str) -> str:
    """Return a welcome email body."""
    return (
        f"Subject: Welcome to {product_name}!\n\n"
        f"Hi there,\n\n"
        f"Thank you for joining the {product_name} community. We're thrilled to have you on board.\n"
        f"Stay tuned for updates and tips to get the most out of {product_name}.\n\n"
        f"Best regards,\n"
        f"The {product_name} Team"
    )


def _schedule_social_posts(product_name: str) -> List[SocialPost]:
    """
    Simulate scheduling social posts for the next 7 days.
    Alternates between Twitter and LinkedIn.
    """
    today = datetime.date.today()
    platforms = ["Twitter", "LinkedIn"]
    posts: List[SocialPost] = []

    for i in range(7):
        platform = platforms[i % len(platforms)]
        content = (
            f"🚀 Launching {product_name} today! "
            f"Check out our new landing page: {_create_landing_page(product_name)}"
        )
        scheduled = today + datetime.timedelta(days=i + 1)  # start tomorrow
        posts.append(
            SocialPost(
                platform=platform,
                content=content,
                scheduled_date=scheduled.isoformat(),
            )
        )
    return posts


def launch_product(product_name: str) -> Dict:
    """
    Orchestrates the one‑click launch workflow.
    Returns a dictionary with all generated artefacts.
    """
    landing_page = _create_landing_page(product_name)
    copy = _generate_copy(product_name)
    email_list_id = _provision_email_list(product_name)
    welcome_email = _draft_welcome_email(product_name)
    social_posts = _schedule_social_posts(product_name)

    result = {
        "product_name": product_name,
        "landing_page_url": landing_page,
        "landing_page_copy": copy,
        "email_list_id": email_list_id,
        "welcome_email": welcome_email,
        "scheduled_posts": [asdict(p) for p in social_posts],
    }
    return result


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="One‑click launch workflow for dev‑marketer."
    )
    parser.add_argument("product_name", help="Name of the product to launch")
    args = parser.parse_args()

    try:
        output = launch_product(args.product_name)
        json.dump(output, sys.stdout, indent=2)
        sys.stdout.write("\n")
    except Exception as exc:  # pragma: no cover
        sys.stderr.write(f"Error: {exc}\n")
        sys.exit(1)
