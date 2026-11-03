// Data model for purchase orders (sample data only)
namespace resoftwa.po;

// A supplier we buy from
entity Vendors {
  key ID : String(10);
  name   : String(80);
  rating : String(10); // good | new | poor
}

// A purchase order
entity PurchaseOrders {
  key poNumber : String(10);
  vendor       : Association to Vendors;
  dueDate      : Date;
  orderedQty   : Integer;
  deliveredQty : Integer;
  amount       : Decimal(15,2);
  virtual isLate : Boolean; // not stored; calculated in the service
}
