### Build imagem
```
docker build -t smtp-relay . 
```

### Exportar as variáveis, conforme exemplo se for linux
```
    export SMTP_HOST="smtp.gmail.com"
    export SMTP_PORT="587"
    export SMTP_USER="abc@gmail.com"
    export SMTP_PASS="token"
    export RELAY_HOST="0.0.0.0"
    export RELAY_PORT="1025"
```

### Executar docker
```
docker run --rm -p 1025:1025 --name smtp-relay smtp-relay
 
```

### Teste
```
telnet localhost 1025
```

Conteúdo da requisição do telnet
```
EHLO example.com
MAIL FROM:<abc@gmail.com>
RCPT TO:<ricardobarcelar@gmail.com>
DATA
Subject: Teste de Assunto
Este é o corpo do e-mail enviado pelo cliente.
.
QUIT
```
