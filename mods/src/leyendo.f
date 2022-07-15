        subroutine leyendo !carga en commons toda la informacion necesaria
               
c para definir los datos de entrada
        character*100 mallaobs
        character*100 nomlineas,fichabun,modelname
        character*100 Stokesfilename
        logical ex        
        real*4 eps(92)
                       
c lugares comunes de memoria para 
        common/ficlineas/nomlineas           !para leelineasii (en StokesFRsub)
        common/fichabun/fichabun
        common/OutputStokes/Stokesfilename   !para escribe_Stokes
        common/abundances/eps
        
c nombre del fichero con los parametros atomicos
        nomlineas='LINEAS'
        
c nombre del fichero con las abundancias
        !fichabun='THEVENIN'        

        !call leeabun(0,eps)
        eps(1) = 12.00
        eps(2) = 10.93
        eps(3) = 1.10
        eps(4) = 1.40
        eps(5) = 2.55
        eps(6) = 8.52
        eps(7) = 7.92
        eps(8) = 8.83
        eps(9) = 4.56 
        eps(10) = 8.08 
        eps(11) = 6.33 
        eps(12) = 7.58 
        eps(13) = 6.47 
        eps(14) = 7.55 
        eps(15) = 5.45 
        eps(16) = 7.33 
        eps(17) = 5.50 
        eps(18) = 6.40 
        eps(19) = 5.12 
        eps(20) = 6.36 
        eps(21) = 3.17 
        eps(22) = 5.02 
        eps(23) = 4.00 
        eps(24) = 5.67 
        eps(25) = 5.39 
        eps(26) = 7.50 
        eps(27) = 4.92 
        eps(28) = 6.25 
        eps(29) = 4.21 
        eps(30) = 4.60 
        eps(31) = 2.88 
        eps(32) = 3.41 
        eps(33) = 2.37 
        eps(34) = 3.41 
        eps(35) = 2.63 
        eps(36) = 3.31 
        eps(37) = 2.60 
        eps(38) = 2.97 
        eps(39) = 2.24 
        eps(40) = 2.60 
        eps(41) = 1.42 
        eps(42) = 1.92 
        eps(43) = 0.00 
        eps(44) = 1.84 
        eps(45) = 1.12 
        eps(46) = 1.69 
        eps(47) = 0.94 
        eps(48) = 1.77 
        eps(49) = 1.66 
        eps(50) = 2.00 
        eps(51) = 1.00 
        eps(52) = 2.24 
        eps(53) = 1.51 
        eps(54) = 2.17 
        eps(55) = 1.13 
        eps(56) = 2.13 
        eps(57) = 1.17 
        eps(58) = 1.58 
        eps(59) = 0.71 
        eps(60) = 1.50 
        eps(61) = 0.00 
        eps(62) = 1.01 
        eps(63) = 0.51 
        eps(64) = 1.12 
        eps(65) = -0.1 
        eps(66) = 1.14 
        eps(67) = 0.26 
        eps(68) = 0.93 
        eps(69) = 0.00 
        eps(70) = 1.08 
        eps(71) = 0.06 
        eps(72) = 0.88 
        eps(73) = -.13 
        eps(74) = 1.11 
        eps(75) = 0.28 
        eps(76) = 1.45 
        eps(77) = 1.35 
        eps(78) = 1.80 
        eps(79) = 1.01 
        eps(80) = 1.13 
        eps(81) = 0.90 
        eps(82) = 1.95 
        eps(83) = 0.71 
        eps(84) = -8.0 
        eps(85) = -8.0 
        eps(86) = -8.0 
        eps(87) = -8.0 
        eps(88) = -8.0 
        eps(89) = -8.0 
        eps(90) = 0.09 
        eps(91) = -8.0 
        eps(92) = -.47
        
c leemos la malla  
        mallaobs='malla.grid'
        call lee_malla(mallaobs)     ! carga el common Malla/ntl,nlin,npas,nble,dlamda
                          
c nombre del fichero de salida con los perfiles de Stokes        
        Stokesfilename='perfil.per'        
        
        return      
        end
