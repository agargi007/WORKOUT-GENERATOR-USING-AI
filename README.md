AI Workout Generator is a web application that leverages Google’s Gemini API to create personalized workout plans based on user-selected fitness goals and experience levels. The project combines a modern, responsive frontend with a Python Flask backend, delivering instant, AI-generated routines and tips tailored to each user.

Project Overview
The landing page presents a clean, user-friendly interface where users select their Fitness Goal (such as Build Muscle, Lose Weight, Increase Endurance, or Improve Flexibility) and Fitness Level (Beginner, Intermediate, Advanced). Upon submission, the backend communicates with the Gemini API, which generates a unique workout plan and actionable tips, displayed in an attractive and readable format.

The application is designed for accessibility and ease of use, with enlarged dropdowns and buttons for better visibility and interaction. Branding is subtly maintained via a watermark, and the UI adapts well to both light and dark themes.

Gemini API Integration
The core intelligence behind the workout generation is provided by Google’s Gemini API, one of the most advanced AI models currently available. Gemini is a multimodal AI developed by Google, capable of understanding and generating text, code, images, and more. In this project, the API is used for natural language processing to create detailed and actionable workout plans based on user input.

Obtaining and Securing a Gemini API Key
To use the Gemini API, you must obtain an API key from Google AI Studio:

Sign in to Google AI Studio
Visit the Google AI Studio website and log in with your Google account.

Generate an API Key
In the dashboard, click “Get API Key” and then “Create API Key in new project.” Name your key for easy identification if prompted.

Copy and Save Your Key
Once generated, copy your API key and store it securely. You will not be able to view it again after navigating away from the page.

Set the API Key as an Environment Variable
For security, do not hard-code your key in your codebase. Instead, set it as an environment variable:

On Linux/macOS, add export GEMINI_API_KEY=your_key_here to your ~/.bashrc or ~/.zshrc, then run source ~/.bashrc or source ~/.zshrc.

On Windows, add GEMINI_API_KEY to your environment variables in system settings.

(Optional) Set Up Billing
Depending on your usage and Google’s current policy, you may need to add billing information to access higher usage tiers.

Using the Gemini API in Your Application
Install the required Python package:

text
pip install google-generativeai
In your Flask backend, import and configure the Gemini API client using your environment variable. When a user submits their goal and level, send this data as a prompt to Gemini and return the generated plan to the frontend.

Key Features
Personalized, AI-generated workout plans and tips

Modern, responsive frontend with enlarged, accessible input elements

Backend powered by Flask for efficient API communication

Secure integration with Gemini API via environment variables

Branding watermark for project identity

Supports both light and dark UI themes

Typical Workflow
User visits the landing page and selects their fitness goal and level.

On submission, the backend sends the user’s selections to the Gemini API.

Gemini responds with a tailored workout plan and tips.

The plan is rendered in a visually appealing format for the user.

Security and Best Practices
Never share your Gemini API key publicly. Always use environment variables to keep your credentials safe.

Monitor your API usage to avoid exceeding quotas and incurring unexpected costs, especially if billing is enabled.

Follow Google’s documentation for the latest updates and best practices for integrating and using the Gemini API.

Use Cases and Extensibility
While this project focuses on fitness plans, the Gemini API supports a wide range of applications, including text summarization, sentiment analysis, translation, and even image and audio processing. The modular backend makes it easy to extend the app with new features or integrate additional AI capabilities in the future.

In summary:
AI Workout Generator is a robust, user-friendly application that demonstrates how to combine modern web development with cutting-edge AI to deliver real value. By following best practices for API key management and leveraging the power of Gemini, this project is both practical and extensible for future enhancements.
