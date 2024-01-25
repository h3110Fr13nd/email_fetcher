# email_fetcher

- Running the selenium chromedriver on docker
- Command to start the container
```bash
docker run -d -p 4444:4444 -p 7900:7900 -p 5900:5900 --shm-size="2g" --name=standalone-chrome selenium/standalone-chrome # :latest or :<tag>
```

```bash
ps -ax | grep "/bin/sh -c cd /home/h3110fr13nd/Desktop/dev/web_scraping/emails_scraper_from_listing_websit" 
```