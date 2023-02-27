# lasergrbl-protocol

online web serial terminal https://bipes.net.br/aroca/web-serial-terminal/

windows terminal https://ttssh2.osdn.jp/ terminal for receive or send data to/from w600-pico

ftp program  https://filezilla-project.org/

https://github.com/arkypita/LaserGRBL/discussions/952

      00000	00352092	log	Recording session started @ 13/04/2020 10:54:11
      00001	00354790	com	Open COM5 @ 115200 baud Ctrl-X
      00002	00354800	tx	[18]
      00003	00354801	tx	[3F]
      00004	00354829	rx	\r
      00005	00354830	rx	Grbl 1.1h ['$' for help]\r
      00006	00354838	rx	<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S|WCO:0.000,0.000,0.000>\r
      00007	00355003	tx	[3F]
      00008	00355010	rx	<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S|Ov:100,100,100>\r
      00009	00355203	tx	[3F]
      00010	00355209	rx	<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S>\r
      00011	00355402	tx	[3F]
      00012	00355408	rx	<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S>\r
      00013	00355604	tx	[3F]
      00014	00355609	rx	<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S>\r
      00015	00355802	tx	[3F]
      00016	00355807	rx	<Idle|MPos:0.000,0.000,0.000|FS:0,0|Pn:S>\r
      [...]
      
      
      	// Handle Grbl Feedback https://github.com/LaserWeb/deprecated-LaserWeb1/blob/master/server.js

	if (data.indexOf('<') == 0) {
		// https://github.com/grbl/grbl/wiki/Configuring-Grbl-v0.8#---current-status

		// remove first <
		var t = data.substr(1);

		// remove last >
		t = t.substr(0,t.length-2);

		// split on , and :
		t = t.split(/,|:/);

		emitToPortSockets(port, 'machineStatus', {'status':t[0], 'mpos':[t[2], t[3], t[4]], 'wpos':[t[6], t[7], t[8]]});

		return;
	}
