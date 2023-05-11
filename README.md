
# News API

This is a simple API built with Flask that returns news articles from the websites. It uses BeautifulSoup to parse the HTML of the website and retrieve the necessary data.

## Usage

To use this API, send a GET request to the `/news` endpoint with the `category` parameter set to one of the available categories:

1. Leave `category` parameter blank for top news
2. national
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. hatke
12. science
13. automobile

For example, to retrieve sports news, you would send a GET request to `https://www.host.com/news?category=sports`.

The API returns a JSON object with the following structure:

```
{
    "success": true,
    "category": "sports",
    "data": [
        {
            "title": "Article title",
            "imageUrl": "https://image.url",
            "url": "https://article.url",
            "content": "Article content",
            "author": "Author name",
            "date": "Article date",
            "time": "Article time",
            "readMoreUrl": "https://read.more.url"
        },
        ...
    ]
}
```

If there is an error retrieving the news articles, the API will return a JSON object with `success` set to `false` and an `errorMessage` field explaining the error.

## Installation

1. Clone this repository: `git clone https://github.com/user/inshorts-news-api.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the server: `python app.py`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
