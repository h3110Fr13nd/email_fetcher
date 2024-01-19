# email_fetcher

- Running the selenium chromedriver on docker
- Command to start the container
```bash
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" --name=standalone-chrome selenium/standalone-chrome # :latest or :<tag>
```

@reboot root sleep 80; ip addr add 127.0.0.53 dev lo; sleep 10; systemctl restart dnsmasq