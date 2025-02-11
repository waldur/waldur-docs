# Terminology

|     Name     |              Description             | Examples |
|:------------:|:------------------------------------:|:--------:|
| Organization  | Legal representation of the entity that can be a client of the Operator. | Ministry A, Department B |
| Project  | Functionality in Self-Service Portal, which allows to group internal resources into projects, which allows to limit access to resources for people.   | Internal systems, Public web |
| Service Provider | Organization can publish offerings in marketplace as soon as it is registered as service provider. | ETAIS, UT HPCC |
| Offering | Service Offering from Service Provider, which can be requested via a Marketplace. Correspond to an entry in the Service Catalogue. | VPS with LB, VDC in DataCenter 1 |
| Category | A grouping of the Offerings defining metadata common to all offerings in this Category. | Compute, Storage, Operations |
| Section | Section is a named aggregate of offering attributes. | System information, Support, Security |
| Attribute | Attribute is an atomic piece of offering metadata, it has name, type and list of options. | Peak TFlop/s, Memory per node (GB) |
| Plan | An option for paying for a particular Offering. There can be multiple options but at each point in time only one Plan can be active. | Small private cloud, Big private cloud |
| Order | A collection of Order items. Considered as done when all Order Items have been processed. | 3 different Offerings with configuration. |
| Order Item | Connects Offering with concrete Organization and configuration settings. | Small VPC with name “test” |
| Resource | Created as part of fulfilling the Order Item. Represents part of the Offering that customer Organization can use. | VM, VPC |
| Category component | Specifies unit of measurement, display name and internal name of the component, which should be present in every category offerings. It is used for aggregating offering component usage and rendering dashboard charts in both project and organization workspace. | vCPU, RAM, storage |
| Offering component | Usage-based component that constitute offering. It may refer to the category component via parent field in order to ensure that component usage is aggregated. | Database count, disk usage |
| Plan Component | Components that constitute a plan. | vCPU, RAM, storage, network bandwidth |
| Component usage | Collects reported resource usage for each plan component separately. | 5 virtual floating IPs for the last month. |
