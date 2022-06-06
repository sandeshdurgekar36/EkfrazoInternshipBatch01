import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-driver',
  templateUrl: './driver.component.html',
  styleUrls: ['./driver.component.css']
})
export class DriverComponent implements OnInit {
  driver!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.driver! = new FormGroup({
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
    return this.driver!.get('driving_license_id');
  }
  get vehicle_status() {
    return this.driver!.get('vehicle_status');
  }
  get badge() {
    return this.driver!.get('badge');
  }
  get license_image() {
    return this.driver!.get('license_image');
  }
  get fitness_certificate_image() {
    return this.driver!.get('fitness_certificate_image');
  }
  get emission_test_image() {
    return this.driver!.get('emission_test_image');
  }
  get insurence_image() {
    return this.driver!.get('insurence_image');
  }
  get rc_image() {
    return this.driver!.get('rc_image');
  }
  get permit_expire_image() {
    return this.driver!.get('permit_expire_image');
  }
  
  

}
