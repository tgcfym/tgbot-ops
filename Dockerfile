FROM alpine:3.20
LABEL org.opencontainers.image.source="https://github.com/tgcfym/tgbot-ops"
LABEL org.opencontainers.image.description="Probe runner for tgcfym.us.ci (小o机器人)"
RUN apk add --no-cache curl jq ca-certificates
WORKDIR /work
CMD ["sh","-c","curl -sS -o /dev/null -w 'tgcfym %{http_code} %{time_total}s\\n' https://tgcfym.us.ci/"]
