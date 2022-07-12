import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { CouponService } from 'src/app/services/coupon.service'; 
import { Router } from '@angular/router';


@Component({
  selector: 'app-coupons',
  templateUrl: './coupons.component.html',
  styleUrls: ['./coupons.component.css']
})
export class CouponsComponent implements OnInit {

  

  constructor(private cService: CouponService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.cuponsform = new FormGroup({
      'id':new FormControl(null, Validators.required),
      'Coupon_name':new FormControl(null, Validators.required),
      'Coupon_discount':new FormControl(null, Validators.required),
      
      
      
      
      
    });
  }
  get id() {
    return this.cuponsform.get('id');
  }
  get Coupon_name() {
    return this.cuponsform.get('Coupon_name');
  }
  get Coupon_discount() {
    return this.cuponsform.get('Coupon_discount');
  }
  cuponsform = this.fb.group({
    id: ['',Validators.required],
    Coupon_name: ['',Validators.required],
    Coupon_discount: ['',Validators.required],
  })
  cupons(){
    console.log(this.cuponsform.value)
    this.cService.cupons(this.cuponsform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}