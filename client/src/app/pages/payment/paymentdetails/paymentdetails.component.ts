import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { PaymentdetService } from 'src/app/services/paymentdet.service'; 
import { Router } from '@angular/router';


@Component({
  selector: 'app-paymentdetails',
  templateUrl: './paymentdetails.component.html',
  styleUrls: ['./paymentdetails.component.css']
})
export class PaymentdetailsComponent implements OnInit {
  

  constructor(private aService: PaymentdetService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.paymentform = new FormGroup({
      'In_order_id':new FormControl(null, Validators.required),
      'amount':new FormControl(null, Validators.required),
      'provider':new FormControl(null, Validators.required),
      'status_id':new FormControl(null, Validators.required),
      'user_id':new FormControl(null, Validators.required),
      
      
      
      
    });
  }
  get In_order_id() {
    return this.paymentform.get('In_order_id');
  }
  get amount() {
    return this.paymentform.get('amount');
  }
  get provider() {
    return this.paymentform.get('provider');
  }
  get status_id() {
    return this.paymentform.get('status_id');
  }
  get user_id() {
    return this.paymentform.get('user_id');
  }
  paymentform = this.fb.group ({
    In_order_id: ['',Validators.required],
    amount: ['',Validators.required],
    provider: ['',Validators.required],
    status_id: ['',Validators.required],
    user_id: ['',Validators.required],
    
  })
  
  payments(){
    console.log(this.paymentform.value)
    this.aService.payments(this.paymentform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}
