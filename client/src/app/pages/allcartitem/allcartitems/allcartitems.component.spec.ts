import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllcartitemsComponent } from './allcartitems.component';

describe('AllcartitemsComponent', () => {
  let component: AllcartitemsComponent;
  let fixture: ComponentFixture<AllcartitemsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AllcartitemsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AllcartitemsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
