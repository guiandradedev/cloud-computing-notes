# Resumo detalhado — Tópicos Avançados de Redes para Datacenter

**Fonte:** *Cloud - Tópicos Avançados de Redes para Datacenter.pdf*  
**Autor dos slides:** Antonio Forster — Escola Politécnica, PUC-Campinas  
**Data indicada no material:** setembro de 2026  
**Quantidade:** 35 slides

## 1. Visão geral

Os slides apresentam uma arquitetura moderna para redes de Data Centers baseada na combinação de:

- **BGP (Border Gateway Protocol):** protocolo de roteamento e troca de informações de alcançabilidade, orientado por políticas e atributos;
- **VXLAN (Virtual Extensible LAN):** tecnologia de encapsulamento que transporta quadros Ethernet sobre uma rede IP;
- **EVPN (Ethernet VPN):** Control Plane baseado em MP-BGP que distribui informações de MAC addresses, IPs, VNIs e localização dos endpoints.

Essa combinação é normalmente implementada sobre uma **Network Fabric Leaf-Spine**. A rede física, chamada **Underlay**, fornece conectividade IP entre os equipamentos. Sobre ela é construída uma rede lógica, chamada **Overlay**, que permite oferecer segmentos Layer 2 virtuais, independentes da topologia física. O VXLAN transporta os dados do Overlay; o BGP EVPN distribui as informações necessárias para que os equipamentos saibam onde estão os destinos.

## 2. Resumo slide a slide

### Slide 1 — Apresentação

O material introduz o tema “Tópicos Avançados de Redes para Datacenter”, apresentado por Antonio Forster, da Escola Politécnica da PUC-Campinas. A aula está situada no contexto de redes de Cloud e Data Centers.

### Slide 2 — Tecnologias e objetivo

São destacados BGP, VXLAN e EVPN. O objetivo é compreender como essas tecnologias são utilizadas em redes modernas de Data Centers e ambientes de Cloud, especialmente em arquiteturas escaláveis e multi-tenant.

### Slide 3 — Da Fabric para BGP e VXLAN

Uma **Network Fabric**, geralmente organizada em topologia **Leaf-Spine**, fornece múltiplos caminhos entre os dispositivos do Data Center. A infraestrutura física pode usar roteamento IP e **ECMP (Equal-Cost Multi-Path)** para distribuir o tráfego entre caminhos de mesmo custo.

Sobre essa rede física pode ser criada uma rede lógica ou Overlay, sem que sua organização precise coincidir com a topologia física. Uma implementação comum usa **VXLAN** no transporte do Overlay e **BGP EVPN** como mecanismo de controle.

### Slide 4 — O que é BGP?

O **BGP** troca informações de alcançabilidade entre diferentes redes IP. Ao contrário de protocolos como OSPF, ele não escolhe caminhos somente pelo menor custo: utiliza políticas, preferências e atributos para decidir qual rota será usada.

O protocolo foi criado principalmente para interligar grandes redes independentes na Internet, isto é, diferentes Autonomous Systems. Hoje também é usado em backbones MPLS e dentro de Data Centers, inclusive em arquiteturas Leaf-Spine e VXLAN/EVPN.

### Slide 5 — Autonomous System (AS)

Um **Autonomous System** é um conjunto de redes administradas segundo uma política de roteamento comum. Cada AS possui um identificador, o **ASN (Autonomous System Number)**.

Operadoras, provedores de Cloud e grandes empresas podem ter seus próprios ASNs. O BGP permite que esses sistemas troquem informações sobre quais redes são alcançáveis por cada um deles.

### Slide 6 — eBGP e iBGP

Quando a sessão BGP conecta roteadores de ASs diferentes, ela é chamada **eBGP (External BGP)**. Quando conecta roteadores pertencentes ao mesmo AS, é chamada **iBGP (Internal BGP)**.

Na Internet, o eBGP é usado principalmente entre organizações e provedores. Em redes corporativas e Data Centers, eBGP e iBGP podem ser usados de acordo com a arquitetura adotada.

### Slide 7 — Funcionamento de uma sessão BGP

Dois roteadores BGP estabelecem uma sessão sobre **TCP**, normalmente na porta **179**. Depois da sessão estabelecida, trocam informações sobre as redes que conseguem alcançar.

O BGP mantém essas informações e seleciona os melhores caminhos com base em atributos e políticas configuradas. Quando há alteração na topologia, normalmente são propagadas apenas as mudanças necessárias, em vez de toda a tabela de rotas ser enviada periodicamente.

### Slide 8 — iBGP, Full Mesh e Route Reflector

Em uma arquitetura iBGP tradicional, os roteadores de um mesmo AS precisam compartilhar entre si as rotas aprendidas. Isso leva a uma topologia **Full Mesh**, na qual cada roteador mantém uma sessão direta com todos os outros.

Esse modelo se torna complexo à medida que o número de roteadores cresce. O **Route Reflector (RR)** reduz a necessidade da malha completa: os roteadores clientes estabelecem sessões com o RR, que reflete os anúncios BGP entre eles.

### Slide 9 — BGP Route Reflector

O slide ilustra o conceito de Route Reflector. A ideia central é centralizar a distribuição de anúncios dentro do AS, reduzindo o número de sessões necessárias e simplificando a operação do iBGP.

### Slide 10 — O que o BGP anuncia?

No funcionamento tradicional, o BGP anuncia **prefixos IP**, informando que determinada rede pode ser alcançada por um roteador ou AS. Um anúncio contém a rede e atributos relacionados ao caminho usado para alcançá-la.

Esses anúncios formam a visão que cada roteador possui sobre os caminhos possíveis. Como exemplo, um roteador pode anunciar que a rede `200.10.20.0/24` é alcançável através de seu Autonomous System.

### Slide 11 — BGP como protocolo Path Vector

O BGP é classificado como protocolo **Path Vector** porque os anúncios carregam informações sobre o caminho percorrido. O atributo principal para isso é o **AS_PATH**, que registra a sequência de ASs atravessados.

Além de indicar que um destino existe, o AS_PATH ajuda a evitar loops: normalmente, um AS rejeita uma rota que contenha o próprio ASN no caminho anunciado.

### Slide 12 — Principais atributos do BGP

Os atributos apresentados são:

- **AS_PATH:** lista de Autonomous Systems atravessados; participa da seleção do caminho e da prevenção de loops;
- **NEXT_HOP:** endereço IP do próximo roteador que deve ser usado para chegar ao destino;
- **LOCAL_PREF:** preferência para escolher caminhos de saída dentro de um AS;
- **MED:** atributo que pode influenciar a entrada de tráfego entre ASs;
- **Communities:** marcações usadas para aplicar políticas de forma organizada;
- **Weight:** preferência local disponível em algumas implementações.

### Slide 13 — Seleção de caminhos no BGP

Um roteador pode receber vários anúncios para o mesmo prefixo. O BGP compara os atributos das rotas e escolhe a melhor de acordo com a política configurada.

Entre os critérios possíveis estão preferências administrativas, LOCAL_PREF, tamanho do AS_PATH, origem da rota, MED e características do próximo salto. O ponto essencial é que a decisão não se resume à menor métrica: o BGP foi projetado para permitir controle político e administrativo do roteamento.

### Slide 14 — BGP versus OSPF

O **OSPF** é um IGP usado principalmente para calcular caminhos dentro de uma rede administrada de forma integrada, tendo como referência principal o menor custo.

O **BGP** foi criado para trocar informações entre domínios e aplicar políticas de roteamento. Em redes grandes, os dois protocolos podem coexistir: OSPF em determinadas funções internas e BGP em outros níveis da arquitetura.

### Slide 15 — BGP em Data Centers

O BGP deixou de ser exclusivo do roteamento entre ASs da Internet e passou a ser usado em grandes Data Centers. A topologia Leaf-Spine combina naturalmente com roteamento IP porque existem vários caminhos paralelos entre Leafs através dos Spines.

Uma implementação comum usa **eBGP entre Leaf e Spine**, atribuindo ASNs diferentes aos equipamentos. O roteamento IP resultante fornece a conectividade básica que será usada posteriormente pelo VXLAN.

### Slide 16 — Vantagens do eBGP na Fabric

O uso de eBGP no Underlay é apresentado como alternativa a protocolos tradicionais ou ao iBGP por três motivos:

1. **Fim dos Route Reflectors:** o eBGP entre vizinhos de ASs diferentes evita a necessidade de Full Mesh iBGP e de Route Reflectors para esse papel;
2. **Prevenção nativa de loops:** o BGP rejeita rotas que contenham o próprio ASN no AS_PATH;
3. **Escalabilidade:** o protocolo foi desenvolvido para lidar com grandes quantidades de rotas e mudanças de topologia.

### Slide 17 — Underlay e Overlay

O **Underlay** é a infraestrutura IP física. Ele conecta os switches e permite que os equipamentos da Fabric alcancem uns aos outros.

O **Overlay** é a rede lógica construída sobre o Underlay. Ele pode representar uma organização diferente da topologia física e criar redes virtuais independentes. O VXLAN é usado para implementar esse Overlay.

### Slide 18 — Limitações das VLANs tradicionais

As VLANs criam domínios Layer 2 sobre uma infraestrutura compartilhada, mas apresentam limitações em Data Centers grandes:

- o identificador VLAN tem 12 bits e oferece aproximadamente 4.000 VLANs utilizáveis;
- a quantidade pode ser insuficiente para ambientes de grande escala e multi-tenant;
- estender domínios Layer 2 aumenta os domínios de broadcast;
- grandes domínios Layer 2 dificultam a escalabilidade e a operação.

Por isso, Data Centers modernos tendem a manter o núcleo predominantemente em Layer 3 e construir redes Layer 2 virtualizadas sobre essa infraestrutura.

### Slide 19 — O que é VXLAN?

**VXLAN (Virtual Extensible LAN)** transporta quadros Ethernet através de uma rede IP. O quadro Ethernet original é encapsulado em um pacote **UDP/IP**, permitindo atravessar uma infraestrutura Layer 3.

Assim, equipamentos conectados a partes diferentes da Fabric podem participar da mesma rede lógica Layer 2. Em outras palavras, o VXLAN cria um Overlay Layer 2 sobre um Underlay Layer 3.

### Slide 20 — Encapsulamento VXLAN

Quando um quadro precisa atravessar a Fabric, o equipamento de entrada acrescenta o cabeçalho VXLAN e, em seguida, os cabeçalhos UDP e IP. A rede física utiliza somente os endereços IP externos para encaminhar o pacote; ela não precisa conhecer diretamente os MACs internos do Overlay.

Ao chegar ao equipamento de destino, os cabeçalhos externos são removidos e o quadro Ethernet original é encaminhado. A porta UDP normalmente usada pelo VXLAN é a **4789**.

### Slide 21 — VNI

Cada rede lógica VXLAN é identificada por um **VNI (VXLAN Network Identifier)** de 24 bits. Isso permite aproximadamente 16 milhões de identificadores, quantidade muito superior às cerca de 4.000 VLANs utilizáveis.

VNIs diferentes representam redes virtuais independentes sobre a mesma infraestrutura IP. Uma VLAN na borda pode ser associada a um VNI para ser transportada pela Fabric.

### Slide 22 — VTEP

O **VTEP (VXLAN Tunnel Endpoint)** encapsula e desencapsula pacotes VXLAN. Em Data Centers, essa função geralmente é executada pelos switches Leaf, embora também possa ser executada por dispositivos virtuais ou hypervisors.

Cada VTEP possui um endereço IP no Underlay, usado como origem ou destino dos pacotes VXLAN. Para o Underlay, a comunicação entre VTEPs parece apenas tráfego IP comum.

### Slide 23 — Comunicação através de VXLAN

Quando um servidor envia um quadro para outro servidor conectado a um Leaf diferente, o VTEP de entrada identifica o VNI correspondente. Ele encapsula o quadro em VXLAN/UDP/IP e usa como destino o endereço IP do VTEP remoto.

Os Spines encaminham o pacote usando apenas o roteamento IP do Underlay. Ao receber o pacote, o VTEP remoto remove o encapsulamento e entrega o quadro Ethernet original ao servidor de destino.

### Slide 24 — O problema da localização dos MACs

O VXLAN define como transportar os quadros, mas não resolve sozinho como um VTEP descobre em qual VTEP remoto está um determinado MAC address.

Uma solução inicial é o **Flood and Learn**, em que tráfego broadcast, unknown unicast e multicast é replicado pelo Overlay para que os VTEPs descubram os destinos. Embora funcional, essa abordagem gera mais tráfego e não escala tão bem em Data Centers grandes.

### Slide 25 — VXLAN Flood and Learn

No Flood and Learn, o VTEP aprende MACs locais observando quadros vindos dos equipamentos conectados. Quando o destino é desconhecido, o tráfego pode ser enviado para vários VTEPs participantes do VNI.

Os VTEPs remotos aprendem a localização dos MACs a partir dos quadros VXLAN recebidos. Em grande escala, o flooding excessivo motiva a adoção de um Control Plane que distribua as informações de forma explícita e eficiente.

### Slide 26 — Da descoberta por flooding ao Control Plane

Em vez de depender apenas da observação do tráfego, cada VTEP pode informar aos demais quais MACs estão conectados localmente. Os outros VTEPs passam a conhecer antecipadamente a localização desses dispositivos, reduzindo a necessidade de replicar tráfego desconhecido.

O mecanismo amplamente utilizado para essa distribuição é **BGP com EVPN**.

### Slide 27 — O que é EVPN?

**EVPN (Ethernet VPN)** é uma tecnologia de Control Plane para distribuir informações de redes Ethernet. Por meio do BGP, o EVPN pode anunciar MAC addresses, endereços IP, VNIs e a localização dos dispositivos na Fabric.

Para isso, usa-se uma extensão do BGP chamada **MP-BGP (Multiprotocol BGP)**. Em uma arquitetura VXLAN/EVPN, o VXLAN transporta os dados e o EVPN distribui as informações necessárias para localizar os destinos.

### Slide 28 — O que é MP-BGP?

O **MP-BGP** permite transportar, na mesma arquitetura de protocolo, informações diferentes das rotas IPv4 tradicionais. Ele pode carregar informações de IPv6, VPNs MPLS e EVPN, entre outras.

A sessão continua sendo BGP sobre TCP na porta 179; o que muda é o tipo de informação carregada nos anúncios. Essa separação permite reutilizar o mecanismo de sessões e atributos do BGP para vários serviços.

### Slide 29 — Address Families no MP-BGP

Uma **Address Family (AF)** identifica o tipo de endereço ou informação de alcançabilidade transportada. O MP-BGP utiliza **AFI (Address Family Identifier)** e **SAFI (Subsequent Address Family Identifier)** para diferenciar os tipos.

O AFI identifica a família geral, como IPv4, IPv6 ou L2VPN. O SAFI detalha o tipo de serviço ou rota dentro dessa família. Uma mesma sessão BGP pode transportar várias famílias, desde que elas sejam negociadas entre os peers.

### Slide 30 — Exemplos de Address Families

O material apresenta os seguintes exemplos:

- **IPv4 Unicast:** prefixos IPv4 tradicionais, como `10.10.0.0/16`;
- **IPv6 Unicast:** prefixos IPv6;
- **VPNv4/VPNv6:** rotas de diferentes VPNs ou clientes em redes MPLS;
- **L2VPN EVPN:** informações de redes Ethernet, incluindo MACs, IPs e dados associados ao Overlay.

### Slide 31 — MP-BGP além das rotas IPv4

O MP-BGP transporta diferentes tipos de **NLRI (Network Layer Reachability Information)**, organizados por Address Families. Isso permite usar o BGP para IPv6, MPLS VPNs, multicast e EVPN, mantendo o mecanismo básico de sessões e troca de atributos.

No VXLAN/EVPN, a família **L2VPN EVPN** permite anunciar MAC addresses, IPs e a localização dos endpoints.

### Slide 32 — Anúncio de um MAC através do BGP EVPN

O exemplo considera uma máquina virtual com MAC `AA:AA:AA:AA:AA:01`, conectada ao Leaf 1 e pertencente ao VNI `10010`.

1. O Leaf 1 aprende localmente o MAC.
2. O Leaf 1 anuncia, via BGP EVPN, que esse MAC pode ser alcançado por ele.
3. O Leaf 2 recebe o anúncio e associa o MAC remoto ao IP do VTEP do Leaf 1.
4. Quando precisar enviar tráfego para esse MAC, o Leaf 2 já sabe qual VTEP deve ser o destino do túnel VXLAN.

O anúncio evita depender de flooding para descobrir a localização do endpoint.

### Slide 33 — EVPN Route Type 2

O EVPN possui diferentes tipos de rotas para transportar informações do Overlay. A **Route Type 2 — MAC/IP Advertisement Route** anuncia a alcançabilidade de MAC addresses e, opcionalmente, os endereços IP associados.

Com esse tipo de rota, o VTEP aprende tanto a localização Layer 2 de um dispositivo quanto informações Layer 3 relacionadas. É o exemplo introdutório mais importante porque mostra como o BGP distribui informações que antes dependiam do aprendizado Ethernet tradicional.

### Slide 34 — Underlay e Overlay juntos

As funções ficam separadas:

- o **Underlay IP** fornece conectividade entre os VTEPs;
- o **BGP EVPN Control Plane** distribui informações sobre dispositivos e redes do Overlay;
- o **VXLAN Data Plane** usa essas informações para encapsular e transportar quadros pela rede IP.

Essa divisão permite que a topologia lógica seja independente da topologia física, aumentando flexibilidade e escalabilidade.

### Slide 35 — Visão geral da combinação

O slide final consolida a arquitetura:

- **BGP:** troca informações de alcançabilidade, aplica políticas e, via MP-BGP, transporta diferentes famílias de informação;
- **VXLAN:** cria um Overlay e transporta quadros Ethernet sobre IP, oferecendo milhões de segmentos lógicos por meio dos VNIs;
- **EVPN:** usa MP-BGP como Control Plane para distribuir MACs e IPs entre VTEPs, reduzindo a dependência de Flood and Learn;
- **Leaf-Spine + IP Underlay + VXLAN + BGP EVPN:** combinação apresentada como uma das arquiteturas mais utilizadas para construir Fabrics escaláveis de Data Centers.

## 3. Como as tecnologias se encaixam

O fluxo completo pode ser entendido em três camadas:

```text
Endpoints/VMs
    |
    | quadros Ethernet e redes virtuais
    v
Leafs / VTEPs
    |  VXLAN: Data Plane, encapsulamento L2 sobre UDP/IP
    |  EVPN: Control Plane, distribuição de MAC/IP/VNI
    v
Spines
    |  Underlay IP, roteamento BGP e ECMP
    v
Outros Leafs / VTEPs
```

Em uma comunicação entre endpoints localizados em Leafs diferentes:

1. O Leaf de origem identifica a rede virtual pelo VLAN/VNI.
2. O VTEP consulta a informação de localização do destino, aprendida localmente ou recebida por EVPN.
3. O quadro Ethernet é encapsulado em VXLAN, UDP e IP.
4. O Underlay encaminha o pacote entre os endereços IP dos VTEPs, usando a Fabric Leaf-Spine.
5. O VTEP remoto desencapsula o pacote e entrega o quadro ao endpoint.

O BGP atua no roteamento do Underlay e também pode atuar no Control Plane do Overlay, por meio do MP-BGP EVPN. O VXLAN fica responsável pelo transporte dos dados do Overlay.

## 4. Conceitos essenciais para revisão

| Conceito | Função principal |
|---|---|
| Leaf-Spine | Topologia de Fabric com vários caminhos entre Leafs e Spines |
| Underlay | Rede física Layer 3 que conecta os equipamentos da Fabric |
| Overlay | Rede lógica construída sobre o Underlay |
| BGP | Troca de rotas e informações de alcançabilidade baseada em políticas |
| eBGP | BGP entre Autonomous Systems diferentes |
| iBGP | BGP dentro do mesmo Autonomous System |
| AS / ASN | Domínio de roteamento e seu identificador |
| ECMP | Distribuição de tráfego por caminhos de mesmo custo |
| VXLAN | Encapsulamento de Ethernet sobre UDP/IP |
| VNI | Identificador de 24 bits de uma rede VXLAN |
| VTEP | Endpoint que encapsula e desencapsula VXLAN |
| EVPN | Control Plane para anunciar informações Ethernet |
| MP-BGP | Extensão do BGP para várias Address Families |
| Route Type 2 | Anúncio EVPN de MAC/IP |
| Flood and Learn | Descoberta de destinos por replicação e observação do tráfego |

## 5. Conclusões

1. **A separação entre Underlay e Overlay é fundamental.** O Underlay fornece conectividade IP simples, enquanto o Overlay implementa redes virtuais que atendem aos requisitos de isolamento e mobilidade dos workloads.

2. **O BGP é adequado para ambientes grandes porque combina escala e políticas.** Em vez de depender exclusivamente de métricas, ele permite selecionar caminhos conforme atributos administrativos e necessidades da organização.

3. **O eBGP simplifica a Fabric Leaf-Spine.** Ao usar ASNs diferentes entre Leafs e Spines, reduz-se a dependência de Full Mesh iBGP e Route Reflectors, além de aproveitar a prevenção de loops pelo AS_PATH.

4. **O VXLAN supera limitações práticas das VLANs.** Seu VNI de 24 bits permite muito mais segmentos lógicos, enquanto o encapsulamento UDP/IP permite atravessar um núcleo Layer 3.

5. **O VTEP é a ponte entre o mundo físico e o virtual.** Ele associa redes locais a VNIs, encapsula quadros para enviá-los pela Fabric e desencapsula tráfego recebido de VTEPs remotos.

6. **O EVPN resolve o problema de descoberta do VXLAN.** O VXLAN transporta os quadros, mas o EVPN informa onde estão os MACs e IPs, reduzindo flooding e tornando a solução mais previsível e escalável.

7. **BGP + VXLAN + EVPN formam uma arquitetura integrada.** BGP fornece roteamento e controle, VXLAN fornece o transporte do Data Plane e EVPN fornece a distribuição de informações do Overlay.

## 6. Síntese em uma frase

Uma Fabric moderna de Data Center usa **eBGP e ECMP no Underlay IP**, **VXLAN para transportar redes Layer 2 virtuais** e **EVPN sobre MP-BGP para anunciar MACs, IPs e VNIs**, obtendo uma infraestrutura escalável, multi-tenant e independente da topologia física.

