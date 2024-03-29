ThreatIntel Queries for threathunting


Email 
| where recipient == "192.168.2.23"
//| count  

OutboundBrowsing
| where src_ip == "192.168.2.97"
| count 

Employees
| where name == "Keith Mitchell"

Email
|where recipient has "envolvelabs"
|where subject contains "vaccine"
|distinct recipient
|count

Email
|where recipient has "envolvelabs"
|where recipient == "Betty Parrish"
//|distinct recipient
|count

Email
//take 10
| where recipient has "betty_parrish"
| count

Email
//take 10
| where recipient has "Parrish"
| count


Email|where recipient has "envolvelabs"|where subject contains "vaccine"|distinct recipient|count

PassiveDns
| where domain contains "vaccine"
| distinct domain
| count

PassiveDns
| where domain has "biotechenvolv.science"

let karen_ips = Employees
| where name has "Karen"
| distinct  ip_addr;
OutboundBrowsing
| where src_ip in (karen_ips)
|count 

Employees
| where ip_addr == "192.168.1.25"

OutboundBrowsing
| where url has "ResearchBibliographyGenerator.zip"

FileCreationEvents
| where filename == “ResearchBibliographyGenerator.zip”

Employees
| where ip_addr == "192.168.1.25"

Email
| where link has "ResearchBibliographyGenerator.zip"

Email
| where subject == "Research opportunties! Apply today"

PassiveDns
| where domain contains "disarm-remarkable.science"

let ips = Email
| where subject == "Research opportunties! Apply today"


PassiveDns
| where domain contains "science"
| where domain contains  

FileCreationEvents
| where filename == "updater.dll"
| where hostname == "DLY5-DESKTOP"
 

Email
//| where sender == "john-n-johnmoderno@yahoo.com"
| where subject has "interview"

Email
| where sender contains "fda"
|where subject == "Research opportunties! Apply today"

