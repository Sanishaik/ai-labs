// Service definition: what the outside world can see
using { resoftwa.po as po } from '../db/schema';

// The OData service, reachable at /odata/v4/po
service POService @(path: '/odata/v4/po') {
  entity Vendors        as projection on po.Vendors;
  entity PurchaseOrders as projection on po.PurchaseOrders;
}
