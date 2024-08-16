package com.example.eureka_service.config;


import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.config.Customizer;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .csrf(csrf -> csrf.disable())  // Disable CSRF
                .authorizeHttpRequests(authz -> authz
                        .requestMatchers("/eureka/**").permitAll()  // Allow all Eureka dashboard and API access
                        .anyRequest().authenticated()
                )
                .httpBasic(Customizer.withDefaults());  // Use basic authentication
//sss
        return http.build();
    }
}

