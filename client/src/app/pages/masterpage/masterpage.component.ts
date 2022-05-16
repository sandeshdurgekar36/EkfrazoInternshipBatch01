import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';

@Component({
  selector: 'app-masterpage',
  templateUrl: './masterpage.component.html',
  styleUrls: ['./masterpage.component.css']
})
export class MasterpageComponent implements OnInit {
  msp1!: FormGroup;
  msp2!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.msp1! = new FormGroup({
      'cname':new FormControl(null, Validators.required),
      'email' : new FormControl(null, [Validators.required, Validators.email]),
      'image':new FormControl(null, Validators.required),          
   });
   this.msp2! = new FormGroup({
      'ucname':new FormControl(null, Validators.required),
      'uemail' : new FormControl(null, [Validators.required, Validators.email]),
      'uimage':new FormControl(null, Validators.required),          
 });
  }
  get cname() {
    return this.msp1!.get('cname');
  }
  get email() {
    return this.msp1!.get('email');
  }
  get image() {
    return this.msp1!.get('image');
  }
  get ucname() {
    return this.msp1!.get('cname');
  }
  get uemail() {
    return this.msp1!.get('email');
  }
  get uimage() {
    return this.msp1!.get('image');
  }
}
