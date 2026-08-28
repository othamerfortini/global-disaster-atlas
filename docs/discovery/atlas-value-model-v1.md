# Global Disaster Atlas — Value & Evidence Model v1

**Status:** Fase 0.3 / proposta para Evidence Specification v1.0
**Data:** 2026-08-28

## 1. Posicionamento

O Atlas não cria números de impacto. Ele agrega, normaliza, relaciona e torna auditáveis observações produzidas por fontes oficiais, científicas e abertas qualificadas.

A unidade fundamental é:

`event -> observations -> evidence -> reconciliation -> canonical representation`

O valor do Atlas está na interoperabilidade, proveniência, detecção/resolução de conflitos, modelagem de cascatas e representação geoespacial.

## 2. Valores de impacto

Cada observação deve preservar:

- `value`
- `value_type`: `exact | estimate | range | minimum | maximum | unknown | conflicting`
- `stage`: `initial_estimate | official_count | revised_estimate | final_estimate | alternative`
- `source`
- `source_record_id`
- `source_url`
- `published_at`
- `observed_at`
- `methodology`
- `definition`
- `unit`
- `geographic_scope`
- `confidence`
- `supersedes` / `superseded_by`

Nenhum valor é convertido de estimativa para contagem exata pelo Atlas.

## 3. Valor canônico

`canonical_value` só é produzido quando as evidências permitem uma escolha defensável.

Quando não permitem, o estado deve ser `conflicting`, `range`, `estimate` ou `unknown` conforme a evidência.

O valor canônico nunca apaga observações alternativas.

## 4. Semântica obrigatória

Distinguir pelo menos:

- deaths
- direct_deaths
- indirect_deaths
- excess_mortality
- injured
- missing
- affected
- exposed
- evacuated
- displaced
- homeless
- physical_damage
- economic_damage
- economic_loss
- reconstruction_needs

`unknown`, `not_reported`, `zero` e `not_applicable` são estados diferentes.

## 5. Cascatas

Eventos compostos devem preservar causalidade e componentes separados.

Exemplo:

`earthquake -> tsunami -> inundation -> evacuation`

Impactos não podem ser somados automaticamente entre componentes quando houver risco de dupla contagem.

## 6. Geografia

Cada impacto espacial pode ter:

- `confirmed`
- `modeled`
- `potential`
- `unknown`

Toda geometria deve possuir proveniência, data, método e nível de confiança quando disponíveis.

O evento pode atingir múltiplos países/regiões.

## 7. Métricas de qualidade

O benchmark mede separadamente:

1. cobertura do campo;
2. proveniência auditável;
3. autoridade da fonte;
4. clareza semântica;
5. consistência temporal;
6. consistência geográfica;
7. transparência metodológica;
8. conflitos identificados;
9. conflitos resolvidos;
10. atribuição causal;
11. confiança espacial;
12. segurança de agregação.

Ter um número disponível não significa que o campo seja plenamente reconstruível.

## 8. Regra de transparência

Toda apresentação pública de um valor crítico deve permitir chegar ao registro original da fonte.

O Atlas deve mostrar explicitamente se o valor é oficial, estimado, revisado, final, intervalar ou conflitante.

## 9. Escopo futuro

A arquitetura deve permitir uma camada operacional de alertas em tempo real sem alterar o modelo histórico de evidência.

`historical evidence layer -> monitoring/ingestion -> near-real-time events -> alerts`

A camada de alertas não deve contaminar retrospectivamente os valores históricos sem preservar versões e proveniência.
