## build Docker image
```shell script
docker build . -f Dockerfile -t pylxd
```

## run the Docker container
```shell script
docker run -p 9090:8080 -v LXDDIR:/lxd -itd pylxd
```
where `LXDDIR` is your certificate files `client.crt` and `client.key` stored.
Now, visit http://127.0.0.1:9090 to use it, change the IP if needed.
