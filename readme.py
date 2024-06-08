import os
import yaml
from datetime import datetime


def get_post_title(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if lines[0].strip() == '---':
            front_matter_lines = []
            for line in lines[1:]:
                if line.strip() == '---':
                    break
                front_matter_lines.append(line)
            front_matter = yaml.safe_load(''.join(front_matter_lines))
            return front_matter.get('title', 'No title found')
    return 'No front matter found'


def extract_date_from_filename(filename):
    # Extract the date part from the filename
    date_str = filename.split('-')[0:3]
    return datetime.strptime('-'.join(date_str), '%Y-%m-%d')


def list_titles_and_dates_in_posts(directory):
    posts = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            title = get_post_title(filepath)
            date = extract_date_from_filename(filename)
            posts.append((filename, title, date))
    return posts


def generate_readme(posts, output_file):
    with open(output_file, 'w', encoding='utf-8') as readme:
        readme.write("# Blog Posts\n\n")
        for filename, title, _ in sorted(posts, key=lambda x: x[2], reverse=True):
            readme.write(f"- [{title}](./_posts/{filename})\n")


if __name__ == '__main__':
    posts_directory = '_posts'
    output_readme = 'README.md'
    posts = list_titles_and_dates_in_posts(posts_directory)
    generate_readme(posts, output_readme)
    print(f"README.md generated with {len(posts)} posts.")
