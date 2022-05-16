import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-addpromocode',
  templateUrl: './addpromocode.component.html',
  styleUrls: ['./addpromocode.component.css']
})
export class AddpromocodeComponent implements OnInit {
  apcode!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.apcode! = new FormGroup({
      'discount':new FormControl(null, Validators.required),
      'qty':new FormControl(null, Validators.required),
      'etstamp':new FormControl(null, Validators.required),
    });
  }
  get discount() {
    return this.apcode!.get('discount');
  }
  get qty() {
    return this.apcode!.get('qty');
  }
  get etstamp() {
    return this.apcode!.get('etstamp');
  }

}
