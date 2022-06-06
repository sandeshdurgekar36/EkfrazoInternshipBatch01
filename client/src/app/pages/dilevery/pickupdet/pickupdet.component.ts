import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-pickupdet',
  templateUrl: './pickupdet.component.html',
  styleUrls: ['./pickupdet.component.css']
})
export class PickupdetComponent implements OnInit {
  pickupd!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.pickupd! = new FormGroup({
      'Customer_address_id':new FormControl(null, Validators.required),
      'pickup_data_time':new FormControl(null, Validators.required),
      'pickup_date':new FormControl(null, Validators.required),
      'pickup_time':new FormControl(null, Validators.required),
      
      
      
      
      
    });
  }
  get Customer_address_id() {
    return this.pickupd!.get('Customer_address_id');
  }
  get pickup_data_time() {
    return this.pickupd!.get('pickup_data_time');
  }
  get pickup_date() {
    return this.pickupd!.get('pickup_date');
  }
  get pickup_time() {
    return this.pickupd!.get('pickup_time');
  }
  
  
  
  

}

