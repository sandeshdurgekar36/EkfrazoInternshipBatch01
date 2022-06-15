import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { VehiclesService } from 'src/app/services/vehicles.service';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router'; 

@Component({
  selector: 'app-vehicle',
  templateUrl: './vehicle.component.html',
  styleUrls: ['./vehicle.component.css']
})
export class VehicleComponent implements OnInit {
  

  constructor(private vService: VehiclesService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.vehicaleform = new FormGroup({
      'vehicleTypeName':new FormControl(null, Validators.required),
      'capacity':new FormControl(null, Validators.required),
      'size':new FormControl(null, Validators.required),
      'details':new FormControl(null, Validators.required),
      'price_per_km':new FormControl(null, Validators.required),
      'min_charge':new FormControl(null, Validators.required),
      'max_time_min':new FormControl(null, Validators.required),
      'badge':new FormControl(null, Validators.required),
      
      
    });
  }
  get vehicleTypeName() {
    return this.vehicaleform.get('vehicleTypeName');
  }
  get capacity() {
    return this.vehicaleform.get('capacity');
  }
  get size() {
    return this.vehicaleform.get('size');
  }
  get details() {
    return this.vehicaleform.get('details');
  }
  get price_per_km() {
    return this.vehicaleform.get('price_per_km');
  }
  get min_charge() {
    return this.vehicaleform.get('min_charge');
  }
  get max_time_min() {
    return this.vehicaleform.get('max_time_min');
  }
  get badge() {
    return this.vehicaleform.get('badge');
  }
  vehicaleform = this.fb.group({
    vehicleTypeName : ['',Validators.required],
    capacity : ['',Validators.required],
    size : ['',Validators.required],
    details : ['',Validators.required],
    price_per_km : ['',Validators.required],
    min_charge : ['',Validators.required],
    max_time_min : ['',Validators.required],
    badge : ['',Validators.required],
  })
  vehicles(){
    console.log(this.vehicaleform.value)
    this.vService.vehicles(this.vehicaleform.value).subscribe(response =>{
      alert("Vheicle Added");
    })
  }

}
