import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { PickupdetService } from 'src/app/services/pickupdet.service'; 
import { Router } from '@angular/router';



@Component({
  selector: 'app-pickupdet',
  templateUrl: './pickupdet.component.html',
  styleUrls: ['./pickupdet.component.css']
})
export class PickupdetComponent implements OnInit {
  

  constructor(private pService: PickupdetService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.pickupdform = new FormGroup({
      'Customer_address_id':new FormControl(null, Validators.required),
      'pickup_data_time':new FormControl(null, Validators.required),
      'pickup_date':new FormControl(null, Validators.required),
      'pickup_time':new FormControl(null, Validators.required),
    });
  }
  get Customer_address_id() {
    return this.pickupdform.get('Customer_address_id');
  }
  get pickup_data_time() {
    return this.pickupdform.get('pickup_data_time');
  }
  get pickup_date() {
    return this.pickupdform.get('pickup_date');
  }
  get pickup_time() {
    return this.pickupdform.get('pickup_time');
  }
  pickupdform =this.fb.group({
    Customer_address_id: ['',Validators.required],
    pickup_data_time: ['',Validators.required],
    pickup_date: ['',Validators.required],
    pickup_time: ['',Validators.required],
  })
  pickups(){
    console.log(this.pickupdform.value)
    this.pService.pickups(this.pickupdform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}
