# docker build -t chatgpt-web-midjourney-proxy . && docker tag chatgpt-web-midjourney-proxy ydlhero/chatgpt-web-midjourney-proxy:v2.11.2 && docker push  ydlhero/chatgpt-web-midjourney-proxy:v2.11.2
git pull
docker build -t openai-signup .
sh deploy.sh
docker logs -f openai-signup-tool