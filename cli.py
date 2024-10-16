import argparse
from app.openai_service import generate_image


def main():
    parser = argparse.ArgumentParser(
        description="Generate car images using OpenAI API."
    )
    parser.add_argument("--model", type=str, required=True, help="The car model")
    parser.add_argument("--color", type=str, required=True, help="The car color")

    args = parser.parse_args()

    try:
        image_url = generate_image(args.model, args.color)
        print(f"Generated Image URL: {image_url}")
    except Exception as e:
        print(f"Error generating image: {str(e)}")


if __name__ == "__main__":
    main()
