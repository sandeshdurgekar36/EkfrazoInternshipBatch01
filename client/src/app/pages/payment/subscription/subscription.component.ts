import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-subscription',
  templateUrl: './subscription.component.html',
  styleUrls: ['./subscription.component.css']
})
export class SubscriptionComponent implements OnInit {
  subs!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.subs!! = new FormGroup({
      'sub_plan_name':new FormControl(null, Validators.required),
      'price':new FormControl(null, Validators.required),
      
    });
  }
  get sub_plan_name() {
    return this.subs!.get('sub_plan_name');
  }
  get price() {
    return this.subs!.get('price');
  }
 


}
