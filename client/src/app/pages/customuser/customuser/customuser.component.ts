import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { CustomuserService } from 'src/app/services/customuser.service'; 
import { Router } from '@angular/router';



@Component({
  selector: 'app-customuser',
  templateUrl: './customuser.component.html',
  styleUrls: ['./customuser.component.css']
})
export class CustomuserComponent implements OnInit {
  

  constructor(private cService: CustomuserService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.customuform = new FormGroup({
      'first_name':new FormControl(null, Validators.required),
      'last_name':new FormControl(null, Validators.required),
      'company_name':new FormControl(null, Validators.required),
      'mobile_number':new FormControl(null, Validators.required),
      'adhaar_card':new FormControl(null, Validators.required),
      'profile_image':new FormControl(null, Validators.required),
      'pancard_image':new FormControl(null, Validators.required),
    });
  }
  get first_name() {
    return this.customuform.get('first_name');
  }
  get last_name() {
    return this.customuform.get('last_name');
  }
  get company_name() {
    return this.customuform.get('company_name');
  }
  get mobile_number() {
    return this.customuform.get('mobile_number');
  }
  get adhaar_card() {
    return this.customuform.get('adhaar_card');
  }
  get profile_image() {
    return this.customuform.get('profile_image');
  }
  get pancard_image() {
    return this.customuform.get('pancard_image');
  }
  customuform = this.fb.group({
    first_name: ['',Validators.required],
    last_name: ['',Validators.required],
    company_name: ['',Validators.required],
    mobile_number: ['',Validators.required],
    adhaar_card: ['',Validators.required],
    profile_image: ['',Validators.required],
    pancard_image: ['',Validators.required],
  })
  custusers(){
    console.log(this.customuform.value)
    this.cService.custusers(this.customuform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}
