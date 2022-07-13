import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { InordService } from 'src/app/services/inord.service'; 
import { Router } from '@angular/router';



@Component({
  selector: 'app-in-order',
  templateUrl: './in-order.component.html',
  styleUrls: ['./in-order.component.css']
})
export class InOrderComponent implements OnInit {
  

  constructor(private iService: InordService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.inplcform = new FormGroup({
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
    return this.inplcform.get('place_order_id');
  }
  get Coupon_id() {
    return this.inplcform.get('Coupon_id');
  }
  get final_amount() {
    return this.inplcform.get('final_amount');
  }
  get comment() {
    return this.inplcform.get('comment');
  }
  get driver_user_id() {
    return this.inplcform.get('driver_user_id');
  }
  get Status_id() {
    return this.inplcform.get('Status_id');
  }
  inplcform = this.fb.group({
    place_order_id: ['',Validators.required],
    Coupon_id: ['',Validators.required],
    final_amount: ['',Validators.required],
    comment: ['',Validators.required],
    driver_user_id: ['',Validators.required],
    Status_id: ['',Validators.required],
    ristrict_no_of_drop: ['',Validators.required],
  })
  inords(){
    console.log(this.inplcform.value)
    this.iService.inords(this.inplcform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}
