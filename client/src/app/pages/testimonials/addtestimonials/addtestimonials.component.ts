import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-addtestimonials',
  templateUrl: './addtestimonials.component.html',
  styleUrls: ['./addtestimonials.component.css']
})
export class AddtestimonialsComponent implements OnInit {
  atestimo!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.atestimo! = new FormGroup({
      'name':new FormControl(null, Validators.required),
      'catag':new FormControl(null, Validators.required),
      'image':new FormControl(null, Validators.required),
      'video':new FormControl(null, Validators.required),
      'rating':new FormControl(null, Validators.required),
      'fsdisc':new FormControl(null, Validators.required),
      'fddisc':new FormControl(null, Validators.required),
    });

  }
  get name() {
    return this.atestimo!.get('name');
  }
  get catag() {
    return this.atestimo!.get('catag');
  }
  get image() {
    return this.atestimo!.get('image');
  }
  get video() {
    return this.atestimo!.get('video');
  }
  get rating() {
    return this.atestimo!.get('rating');
  }
  get fsdisc() {
    return this.atestimo!.get('fsdisc');
  }
  get fddisc() {
    return this.atestimo!.get('fddisc');
  }

}
