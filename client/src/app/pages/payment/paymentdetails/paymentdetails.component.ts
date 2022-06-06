import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-paymentdetails',
  templateUrl: './paymentdetails.component.html',
  styleUrls: ['./paymentdetails.component.css']
})
export class PaymentdetailsComponent implements OnInit {
  payment!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.payment! = new FormGroup({
      'In_order_id':new FormControl(null, Validators.required),
      'amount':new FormControl(null, Validators.required),
      'provider':new FormControl(null, Validators.required),
      'status_id':new FormControl(null, Validators.required),
      'user_id':new FormControl(null, Validators.required),
      
      
      
      
    });
  }
  get In_order_id() {
    return this.payment!.get('In_order_id');
  }
  get amount() {
    return this.payment!.get('amount');
  }
  get provider() {
    return this.payment!.get('provider');
  }
  get status_id() {
    return this.payment!.get('status_id');
  }
  get user_id() {
    return this.payment!.get('user_id');
  }
  
  

}
