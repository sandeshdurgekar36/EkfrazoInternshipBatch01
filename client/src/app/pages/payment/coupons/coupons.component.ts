import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-coupons',
  templateUrl: './coupons.component.html',
  styleUrls: ['./coupons.component.css']
})
export class CouponsComponent implements OnInit {

  cupons!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.cupons! = new FormGroup({
      'id':new FormControl(null, Validators.required),
      'Coupon_name':new FormControl(null, Validators.required),
      'Coupon_discount':new FormControl(null, Validators.required),
      
      
      
      
      
    });
  }
  get id() {
    return this.cupons!.get('id');
  }
  get Coupon_name() {
    return this.cupons!.get('Coupon_name');
  }
  get Coupon_discount() {
    return this.cupons!.get('Coupon_discount');
  }

}
