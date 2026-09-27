## Tipos de serviços e Responsabilidade Compartilhada

### Tipos de Serviço

#### IaaS: Infrastructure as a Service

É a **categoria mais flexível de cloud**, permite **locação de infraestrutura** como um serviço. Nela o provedor é responsável por manter o hardware, conectividade de rede e segurança física, enquanto o consumidor é responsável por todo o resto, desde configurar e manter o SO, até lidar com a aplicação.

##### Cenários

###### Migração _Lift-and-shift_

Processo de transformação inicial na migração para nuvem, configurando recursos de forma semelhante ao original.
Um processo encontrado nesta etapa é o P2V (Physical to Virtual), que gera uma imagem de sistema bootavel para virtualizar no formato Hypervisor, convertendo o SO com drivers de CPU físico (ex. Intel Core XX) para uma CPU genérica.

##### Teste e desenvolvimento

O consumidor define configurações de ambiente para replicação rápida.

#### PaaS: Platform as a Service

**Locação de plataforma para deployment**. Em um ambiente PaaS, o **provedor mantém as responsabilidades** que mantinha em um **IaaS**, mas adicionalmente também é **responsável por manter o SO, middlewares, ferramentas de desenvolvimento** etc. Enquanto isso, o **cliente não precisa se preocupar com licença ou atualizações de SOs**, **focando no processo de desenvolvimento de software** sem comprometer a infraestrutura de execução.

##### Cenários

[...]

##### PaaS com Orquestração de Containers: Docker Swarm e Kubernetes

- **Escalabilidade automatizada com múltiplos Pods**: garante resiliência e balanceamento de carga automatico conforme a demanda.
- **Orquestração com Kubernetes**: autoescalonamento, rollouts automáticos, gerenciamento de estado desejados. Garantindo alta disponibilidade e manutenção contínua sem downtime.
- **Swarm como alternativa simples**: orquestração básica de serviços integrada ao Docker com menos complexidade operacional.
- **Automação de deploys e monitoramenteo**: integração de pipelines CI/CD e ferramentas de monitoramento, reduzindo esforço manual na manutenção e confiabilidade da operação.
- **Responsabilidade compartilhada na orquestração**: provedor gerencia a infra e a plataforma de orquestração, enquanto o cliente lida com as configurações do serviço, políticas de escalabilidade e segurança dos containers.

#### SaaS: Software as a Service

Modelo de serviço mais completo a nível de produto, **alugando um aplicativo desenvolvido, instalado e configurado**, como por exemplo e-mail, CRM etc. **Menos flexível mas mais fácil de iniciar o uso**, necessitando de menos conhecimento técnico.

##### Cenários

[...]

### Responsabilidade Compartilhada nos Diferentes Modelos de Serviço em Cloud

Cada modelo de serviço possui uma divisão específicas de responsabilidades

#### IaaS

##### Responsabilidades do Provedor

- **Infraestrutura física**: gerenciamento e manutenção dos servidores, redes e storage;
- **Segurança física**: controle de acesso físico;
- **Disponibilidade**: garantia de uptime da infra e provisionamento de recursos.

##### Responsabilidades do Cliente

- **SO**: instalação, configuração e manutenção;
- **Segurança de rede**: configuração e gerenciamento de firewalls e grupos de segurança;
- **Dados e aplicativos**

##### Detalhes adicionais

###### Monitoramento e Logging

- **Provedor**: ferramentas básicas para monitoramento da infra;
- **Cliente**: monitorar o desempenho e segurança do sistema.

###### Patching e Atualizações

- **Provedor**: patches na infra física e hypervisor;
- **Cliente**: patches no SO da VM e em softwares instalados.

###### Escalaiblidade e Elasticidade

- **Provedor**: capacidades de escalabilidade automática;
- **Cliente**: configurar políticas de escalabilidade.
  
#### PaaS

##### Responsabilidades do Provedor

- **Infraestrutura e plataforma**: gerenciamento da infraestrutura subjacente e ferramentas de dev;
- **Segurança do ambiente**: aplicação de patches e atualizações de segurança;
- **Disponibilidade da plataforma**: garantia de uptime e manutenção dos serviços.

##### Responsabilidades do Cliente

- **Desenvolvimento de aplicativos**;
- **Gerenciamento de dados**: proteção e conformidade dos dados usados;
- **Configuração de acesso**: controle de acesso e permissões, tanto na aplicação quanto no acesso a cloud (tal qual AWS IAM).

##### Detalhes adicionais

###### Integração e API Management

- **Provedor**: fornecer APIs e serviços integrados;
- **Cliente**: integrar serviços de terceiros e gerenciar dependências de API.

###### Segurança de Aplicativos

- **Provedor**: garantir segurança no ambiente de execução e ferramentas;
- **Cliente**: garantir segurança dentro dos apps (RBAC).

###### Escalabilidade

- **Provedor**: fornecer mecanismos de escalabilidade automática
- **Cliente**: configurar políticas de escalabilidade

#### SaaS

##### Responsabilidades do Provedor

- **Aplicativo e infraestrutura**: gerenciamento total do software e infra;
- **Segurança e conformidade**: garantir segurança, proteção de dados e conformidade com regulamentos;
- **Disponibilidade e desempenho**.

##### Responsabilidades do Cliente

- **Gerenciamento de acessos**;
- **Proteção de dados**: garantia de integridade e segurança dos dados inseridos;
- **Conformidade de uso**.

##### Detalhes adicionais

###### Configuração e Personalização

- **Provedor**: fornecer opções de personalização dentro dos limites da aplicação;
- **Cliente**: configurar para atender às necessidades de negócio.

###### Backup e Recuperação de Dados

- **Provedor**: backups regulares e recuperação em caso de falha;
- **Cliente**: poder solicitar backups adicionais e gerir dados de acordo com políticas de retenção.

###### Atualizações Automáticas

- **Provedor**: atuaolizações automáticas;
- **Cliente**: ajustar fluxos de trabalho em resposta às atualizações.

#### Comparação entre modelos

- **IaaS**: maior **controle** e **responsabilidade do cliente**
- **PaaS**: responsabilidades **equilibradas**, com **foco** do cliente **no desenvolvimento** e segurança dos apps.
- **SaaS**: responsabilidade **mínima** para o cliente, focado principalmente na gestão de acesso e uso seguro dos dados.

![Responsabilidade entre modelos](../assets/responsabilidade.png)

#### Considerações sobre segurança

Para garantir a eficácia na segurança, é necessário colaboração entre cliente e provedor, implementando práticas robustas em cada camada.
Alguns dos riscos comuns incluem:
- **IaaS**: falha na configuração do SO e rede;
- **PaaS**: vulnerabilidade em apps;
- **SaaS**: gestão inadequada de acessos.

#### Desafios

- **Complexidade e escalabilidade** em especial em ambientes híbridos dificultam com muitos níveis de controle e responsabilidade;
- **Conformidade** para evitar violações de conformidade e penalidades regulatórias;
- **Monitoramento contínuo** para garantir que todas as responsabilidades estão sendo cumpridas.

#### Boas práticas

- **Contratos claros** definindo resopnsabilidades de cada parte;
- **Educação contínua** através de treinamentos;
- **Ferramentas de segurança e monitoramento** para garantir segurança e desempenho contínuo.