SELECT MONTHNAME(charged_datetime) AS month, SUM(amount) AS revenue
FROM billing
WHERE charged_datetime >= '2012-03-01' AND charged_datetime <= '2012-03-31';

SELECT clients.client_id, SUM(amount) AS total_revenue
FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

SELECT sites.domain_name AS websites, clients.client_id
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 10;

SELECT clients.client_id, COUNT(sites.domain_name) AS number_of_websites, MONTHNAME(created_datetime) AS month_created, YEAR(created_datetime) AS year_created
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 1
GROUP BY MONTH(created_datetime), YEAR(created_datetime)
ORDER BY sites.site_id;

SELECT sites.domain_name, COUNT(leads.leads_id) AS number_of_leads, leads.registered_datetime AS date_generated
FROM sites
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime <= '2011-02-15' AND leads.registered_datetime >= '2011-01-01'
GROUP BY sites.domain_name
ORDER BY sites.site_id;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.site_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31' 
GROUP BY clients.first_name
ORDER BY number_of_leads DESC;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads_id) AS number_of_leads, MONTHNAME(registered_datetime) AS month_generated
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime BETWEEN '2011/01/01' AND '2011/06/01'
GROUP BY sites.site_id
ORDER BY registered_datetime, clients.client_id DESC;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, 
sites.domain_name AS websites, COUNT(leads_id) AS number_of_leads,
registered_datetime AS date_generated
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime BETWEEN '2011/01/01' AND '2011/12/31'
GROUP BY sites.client_id, sites.site_id;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, 
SUM(amount) AS Total_Revenue, 
MONTHNAME(charged_datetime) AS month,
YEAR(charged_datetime) AS year
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, YEAR(billing.charged_datetime), MONTH(billing.charged_datetime);

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, 
GROUP_CONCAT(sites.domain_name separator ' / ') AS sites
FROM clients
JOIN sites ON clients.client_id = sites.client_id
GROUP BY client_name
ORDER BY clients.client_id