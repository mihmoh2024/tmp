@startuml
left to right direction
skinparam packageStyle rect
actor клиент
actor банк
rectangle банкомат {
  клиент--(проверка баланса)
  клиент--(снятие наличных)
  клиент--(положить деньги на карту)
  (снятие наличных) .> (проверка баланса)
  банк--(проверить остатки наличных)
  банк--(мониторинг работоспособности)
}
@enduml



![image](https://github.com/mihmoh2024/tmp/assets/89910305/fc6457bb-4472-4ba6-9024-2603cffd3657)
