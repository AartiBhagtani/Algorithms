requirements:
  take orders from customers
  submiting the order to kitchen
  deliver the order back to customers
  sharing the total bill to customers
  
assump:
  kitchen apis - ready
  customer arrival, dept - ready

customer:
  table_id

menu_items:
  food_id
  food_name
  food_price  

orders:
  order_id
  table_id
  ordered_items(menu_items)

robots:
  robot_id 
  table
  order_id
  central_system_event
  kitchen(order_id)
  
table:
  table_id
  table_status(free, occupied)

<!-- multiple robots table scenario -->
robot:
  robot_id
  robot_status

monitoring_system:
  robot
  tables
  queue 
  
table:
  table_id
  table_request
  table_status(free, occupied)
  

<!-- async function get_location(() => {
  get('http://....')
}) -->