import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-customuser',
  templateUrl: './customuser.component.html',
  styleUrls: ['./customuser.component.css']
})
export class CustomuserComponent implements OnInit {
  customu!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.customu! = new FormGroup({
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
    return this.customu!.get('first_name');
  }
  get last_name() {
    return this.customu!.get('last_name');
  }
  get company_name() {
    return this.customu!.get('company_name');
  }
  get mobile_number() {
    return this.customu!.get('mobile_number');
  }
  get adhaar_card() {
    return this.customu!.get('adhaar_card');
  }
  get profile_image() {
    return this.customu!.get('profile_image');
  }
  get pancard_image() {
    return this.customu!.get('pancard_image');
  }

}
