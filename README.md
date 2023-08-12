# Gestão de RH - Escopo
- [ ] Cadastro de empresa [MESMA TELA DO ONBOARDING]
- [ ] Login de usuário de RH da empresa parceira
- [ ] Header do portal
- [ ] Chat entre plataformas
- [ ] Menu lateral para navegação
- [ ] Dashboards
- [ ] Gestão de funcionários
- [ ] Gestão de Welcome Kits
- [ ] Tela de feedbacks
- [ ] Gamificação
- [ ] Meu perfil

## Banco de dados

### Criando e rodando banco

```bash
cd docker-rh
sudo docker build -f Dockerfile -t mysql_db .
sudo docker run -p 3306:3306 -d --name banco_onboarding -v mysql-volume:/var/lib/mysql mysql_db
```

### Rodando

```bash
sudo docker start banco_onboarding
```
