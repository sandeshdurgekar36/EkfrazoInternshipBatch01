import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-importuser',
  templateUrl: './importuser.component.html',
  styleUrls: ['./importuser.component.css']
})
export class ImportuserComponent implements OnInit {
  imuser!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.imuser! = new FormGroup({
      'image':new FormControl(null, Validators.required),
    });
  }
  get image() {
    return this.imuser!.get('image');
  }
}
