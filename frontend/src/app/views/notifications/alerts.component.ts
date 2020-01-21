import { Component, SecurityContext, ViewEncapsulation } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { AlertConfig } from 'ngx-bootstrap/alert';

// such override allows to keep some initial values

export function getAlertConfig(): AlertConfig {
  return Object.assign(new AlertConfig(), { type: 'success' });
}

@Component({
  templateUrl: 'alerts.component.html',
  encapsulation: ViewEncapsulation.None,
  styles: [
    `
  .alert-md-local {
    background-color: #009688;
    border-color: #00695C;
    color: #fff;
  }
  `
  ],
  providers: [{ provide: AlertConfig, useFactory: getAlertConfig }]
})
export class AlertsComponent {

  constructor(sanitizer: DomSanitizer) {
    this.alertsHtml = this.alertsHtml.map((alert: any) => ({
      type: alert.type,
      msg: sanitizer.sanitize(SecurityContext.HTML, alert.msg)
    }));
  }
  dismissible = true;
  alerts: any = [
    {
      type: 'danger',
      msg: `La temperature de l'air est en dessous de 25°C.`
    },
    {
      type: 'info',
      msg: `Le PH du sol diminue dangeureusement`
    },
    {
      type: 'danger',
      msg: `La temperature du noeud1 est en dessous de 25°C.`
    }
  ];

  alertsHtml: any = [
    {
      type: 'success',
      msg: ` Votre arrosage a l'eau du 10-03-2020 a 10h35 s'est bien effectuee.`
    },
    {
      type: 'success',
      msg: ` Votre arrosage a l'eau fertilise du 10-03-2020 a 10h50 s'est bien effectuee.`
    },
    {
      type: 'danger',
      msg: `Votre arrosage du 11-03-2020 a 13h35 a echoue.`
    }
  ];

  index = 0;
  messages = [
    'You successfully read this important alert message.',
    'Now this text is different from what it was before. Go ahead and click the button one more time',
    'Well done! Click reset button and you\'ll see the first message'
  ];

  alertsDismiss: any = [];

  reset(): void {
    this.alerts = this.alerts.map((alert: any) => Object.assign({}, alert));
  }

  changeText() {
    if (this.messages.length - 1 !== this.index) {
      this.index++;
    }
  }

  add(): void {
    this.alertsDismiss.push({
      type: 'info',
      msg: `This alert will be closed in 5 seconds (added: ${new Date().toLocaleTimeString()})`,
      timeout: 5000
    });
  }
}
