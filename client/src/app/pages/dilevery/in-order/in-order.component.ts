import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-in-order',
  templateUrl: './in-order.component.html',
  styleUrls: ['./in-order.component.css']
})
export class InOrderComponent implements OnInit {
  inplc!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.inplc! = new FormGroup({
      'place_order_id':new FormControl(null, Validators.required),
      'Coupon_id':new FormControl(null, Validators.required),
      'final_amount':new FormControl(null, Validators.required),
      'comment':new FormControl(null, Validators.required),
      'driver_user_id':new FormControl(null, Validators.required),
      'Status_id':new FormControl(null, Validators.required),
      'ristrict_no_of_drop':new FormControl(null, Validators.required),
      
      
      
    });
  }
  get place_order_id() {
    return this.inplc!.get('place_order_id');
  }
  get Coupon_id() {
    return this.inplc!.get('Coupon_id');
  }
  get final_amount() {
    return this.inplc!.get('final_amount');
  }
  get comment() {
    return this.inplc!.get('comment');
  }
  get driver_user_id() {
    return this.inplc!.get('driver_user_id');
  }
  get Status_id() {
    return this.inplc!.get('Status_id');
  }
  
  

}
