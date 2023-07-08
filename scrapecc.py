import requests
from bs4 import BeautifulSoup
import csv

# Fetch the blog page
response = requests.get('https://aws.amazon.com/blogs/contact-center/')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all blog posts
posts = soup.find_all('div', class_='blog-post')

# Prepare for CSV output
with open('aws_blog_posts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Summary", "URL"])

    # Extract and write data for each post
    for post in posts:
        title = post.find('h2').text
        summary = post.find('p').text
        url = post.find('a')['href']

        writer.writerow([title, summary, url])

