FROM denoland/deno:alpine

COPY . .

RUN deno install

CMD ["deno", "main.ts"]
