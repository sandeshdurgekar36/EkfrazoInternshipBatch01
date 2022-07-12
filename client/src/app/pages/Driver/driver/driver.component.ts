import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { DriverService } from 'src/app/services/driver.service'; 
import { Router } from '@angular/router';



@Component({
  selector: 'app-driver',
  templateUrl: './driver.component.html',
  styleUrls: ['./driver.component.css']
})
export class DriverComponent implements OnInit {
  

  constructor(private dService: DriverService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.driverform = new FormGroup({
      'driving_license_id':new FormControl(null, Validators.required),
      'vehicle_status':new FormControl(null, Validators.required),
      'badge':new FormControl(null, Validators.required),
      'license_image':new FormControl(null, Validators.required),
      'fitness_certificate_image':new FormControl(null, Validators.required),
      'emission_test_image':new FormControl(null, Validators.required),
      'insurence_image':new FormControl(null, Validators.required),
      'rc_image':new FormControl(null, Validators.required),
      'permit_expire_image':new FormControl(null, Validators.required),
      
      
      
      
    });
  }
  get driving_license_id() {
    return this.driverform.get('driving_license_id');
  }
  get vehicle_status() {
    return this.driverform.get('vehicle_status');
  }
  get badge() {
    return this.driverform.get('badge');
  }
  get license_image() {
    return this.driverform.get('license_image');
  }
  get fitness_certificate_image() {
    return this.driverform.get('fitness_certificate_image');
  }
  get emission_test_image() {
    return this.driverform.get('emission_test_image');
  }
  get insurence_image() {
    return this.driverform.get('insurence_image');
  }
  get rc_image() {
    return this.driverform.get('rc_image');
  }
  get permit_expire_image() {
    return this.driverform.get('permit_expire_image');
  }
  driverform = this.fb.group({
    driving_license_id: ['',Validators.required],
    vehicle_status: ['',Validators.required],
    badge: ['',Validators.required],
    license_image: ['',Validators.required],
    fitness_certificate_image: ['',Validators.required],
    emission_test_image: ['',Validators.required],
    insurence_image: ['',Validators.required],
    rc_image: ['',Validators.required],
    permit_expire_image: ['',Validators.required], 
  })
  drivers(){
    console.log(this.driverform.value)
    this.dService.drivers(this.driverform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}